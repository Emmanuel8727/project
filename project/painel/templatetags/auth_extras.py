from django import template
from login.utils import verificar_grupo  # Importa a função que verifica usuario e grupo

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    '''Repassa a verificação de grupo para a função compartilhada do app login.'''
    return verificar_grupo(user, group_name)
