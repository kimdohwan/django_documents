from django.db import models

__all__ = (
    'TwitterUser',
    'Relation'
)


class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
    )

    def __str__(self):
        return self.name


class Relation(models.Model):
    CHOICE_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user',
    )
    relation_type = models.CharField(
        max_length=1,
        choices=CHOICE_RELATION_TYPE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'from({}), to({}), {}'.format(
            self.from_user,
            self.to_user,
            self.get_relation_type_display(),
        )