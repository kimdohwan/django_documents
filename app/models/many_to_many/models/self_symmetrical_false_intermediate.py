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

# 두 프로퍼티에서 리턴하는 방식이 다르다
# 둘이 어떻게 다른지 알자
# block_relations에 써준 방식이 더 보기 쉽다
    @property
    def following(self):
        # 내가 follow하고 있는 Relation들을 리턴
        return Relation.objects.filter(from_user=self, relation_type='f')

    @property
    def block_relations(self):
        return self.relations_by_from_user.filter(relation_type='b')

    @property
    def follower_relations(self):
        return self.relations_by_to_user.filter(relation_type='f')


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