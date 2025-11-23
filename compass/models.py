from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Instruction(models.Model):
    DIRECTION_CHOICES = [
        ('N', 'North'),
        ('NE', 'North-East'),
        ('E', 'East'),
        ('SE', 'South-East'),
        ('S', 'South'),
        ('SW', 'South-West'),
        ('W', 'West'),
        ('NW', 'North-West'),
    ]

    # Directions mapped to degrees for SVG rotation in the template
    DIRECTION_DEGREES = {
        'N': 0, 'NE': 45, 'E': 90, 'SE': 135,
        'S': 180, 'SW': 225, 'W': 270, 'NW': 315
    }

    direction = models.CharField(max_length=2, choices=DIRECTION_CHOICES)
    distance = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Distance in nautical miles (must be positive)"
    )
    description = models.TextField(
        help_text="Details about landmarks or hazards")
    risk_level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Risk level from 0 (safe) to 100 (deadly)"
    )

    # Self-referencing Foreign Key to create the linked list of instructions
    previous_instruction = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_step',
        verbose_name="Previous Instruction"
    )

    def get_rotation_degrees(self):
        """Returns degrees for CSS rotation based on direction."""
        return self.DIRECTION_DEGREES.get(self.direction, 0)

    def get_route_summary(self):
        """
        Traverses the linked list backwards to calculate stats 
        from the start of the chain up to this instruction.
        """
        total_distance = 0
        total_risk = 0
        count = 0

        current = self
        while current:
            total_distance += current.distance
            total_risk += current.risk_level
            count += 1
            current = current.previous_instruction

        avg_risk = total_risk / count if count > 0 else 0
        return {
            'total_distance': total_distance,
            'average_risk': round(avg_risk, 1),
            'step_count': count
        }

    def __str__(self):
        return f"#{self.id} - {self.distance}nm {self.get_direction_display()}"
# Create your models here.
