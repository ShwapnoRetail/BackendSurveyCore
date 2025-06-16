from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SurveyType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    site_id = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    survey_type = models.ForeignKey(SurveyType, on_delete=models.SET_NULL, null=True)
    is_location_based = models.BooleanField(default=False)
    is_image_required = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user_id = models.IntegerField()

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPES = [
        ('yesno', 'Yes/No'),
        ('text', 'Text'),
        ('choice', 'Multiple Choice'),
        ('image', 'Image Upload'),
        ('location', 'Location'),
    ]

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    has_marks = models.BooleanField(default=False)
    marks = models.PositiveIntegerField(blank=True, null=True)
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.text[:50]}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class SurveyTarget(models.Model):
    TARGET_CHOICES = [
        ('user', 'Individual User'),
        ('department', 'Department'),
        ('site', 'Site/Outlet'),
        ('role', 'Role'),
        ('all', 'All Users'),
    ]

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='targets')
    target_type = models.CharField(max_length=20, choices=TARGET_CHOICES)
    user_id = models.IntegerField(null=True, blank=True)  # Central system user ID
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    site_id = models.IntegerField(null=True, blank=True)  # From central system
    role_name = models.CharField(max_length=50, null=True, blank=True)  # e.g., 'OutletManager'

    def __str__(self):
        return f"{self.survey.title} -> {self.target_type}"


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.survey.title} by {self.user_id}"


class Answer(models.Model):
    response = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)
    selected_choice = models.ForeignKey(Choice, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='survey_answers/images/', blank=True, null=True)
    marks_obtained = models.PositiveIntegerField(null=True, blank=True)
    is_admin_submission = models.BooleanField(default=False)
    submitted_by = models.JSONField(default=dict)  # Stores user info from JWT

    def save(self, *args, **kwargs):

        if not self.submitted_by and hasattr(self, '_request_user'):
            self.submitted_by = {
                'user_id': self._request_user['user_id'],
                'username': self._request_user['username'],
                'email': self._request_user['email'],
                'is_admin': self._request_user['is_admin']
            }
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Answer to Q{self.question.id} in response {self.response.id}"

    class Meta:
        unique_together = ['response', 'question']  # One answer per question per response

    def __str__(self):
        return f"Answer to Q{self.question.id} by {self.submitted_by.get('username', 'unknown')}"