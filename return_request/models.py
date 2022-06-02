from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ReturnOrderRequest(models.Model):
    """Return request model."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="return_order_requests",
        null=False,
        blank=False,
    )
    order = models.ForeignKey(
        "order.Order",
        on_delete=models.CASCADE,
        related_name="return_order_requests",
        null=False,
        blank=False,
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=32,
        choices=[
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="pending",
    )

    def __str__(self):
        return self.user
