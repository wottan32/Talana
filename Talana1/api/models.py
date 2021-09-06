from django.db import models


class ClUserData(models.Model):
    rut = models.CharField('RUT', primary_key=True, max_length=12, null=False, blank=False)
    Nombre = models.CharField('Nombre', max_length=50, null=False, blank=False)
    Apellido_1 = models.CharField('Apellido_1', max_length=50,
                                  null=False, blank=False)
    Apellido_2 = models.CharField('Apellido_2', max_length=50,
                                  null=False, blank=False)
    mail = models.CharField('mail', max_length=300,
                            null=False, blank=False)


class InvitationToken(models.Model):
    code = models.CharField(max_length=12, unique=True, blank=True)
    token = models.CharField(max_length=40, unique=True, editable=False)

    uses = models.PositiveIntegerField(
        default=1, blank=True, null=True,
        help_text='este numero servira solo una vez')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created)

    def save(self, **kwargs):
        if not self.id:
            if not self.code:
                self.code = get_random_string()
        self.token = uuid4().hex
        return super(InvitationToken, self).save(**kwargs)
