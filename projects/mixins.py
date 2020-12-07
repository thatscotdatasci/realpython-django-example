from .models import IMG_REL_PATH


class ProjectImageContextMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['img_rel_path'] = IMG_REL_PATH
        return context
