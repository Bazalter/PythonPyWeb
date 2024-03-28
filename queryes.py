import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы
    #
    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)
    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(obj)
    # inner_qs = Blog.objects.filter(name__contains='Путешествия')
    # entries = Entry.objects.filter(blog__in=inner_qs)
    # print(entries)
    # all_obj = Blog.objects.all()
    # for idx, value in enumerate(all_obj):
    #     print(f"idx = {idx}, value = {value}")
    # print(Blog.objects.filter(id=2, name="Путешествия по миру").exists())
    # print(Blog.objects.count())








