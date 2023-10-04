from django.core.files.storage import FileSystemStorage


class FileSystemOverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return super().get_available_name(name, max_length)