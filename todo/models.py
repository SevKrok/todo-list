from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_completed", "-created_at"]

    def __str__(self):
        return (f"{self.content} "
                f"(Tags: {[tag.name for tag in self.tags.all()]})")
