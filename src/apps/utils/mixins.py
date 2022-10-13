from django.core.exceptions import PermissionDenied


class AdminRequiredMixin:
    permisos_requeridos = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            # if not request.user.is_superuser:
            #     raise PermissionDenied

            if self.permisos_requeridos:
                tiene_permiso = False

                grupos_user = request.user.groups.all()
                if grupos_user:
                    for g in grupos_user:
                        if g.permissions.all().filter(codename__in=self.permisos_requeridos).exists():
                            tiene_permiso = True
                            break
                else:
                    if request.user.user_permissions.filter(codename__in=self.permisos_requeridos).exists():
                        tiene_permiso = True

                if not tiene_permiso:
                    raise PermissionDenied

        return super(AdminRequiredMixin, self).dispatch(request, *args, **kwargs)
