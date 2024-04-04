from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])  # TODO Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        self.answer2 = Author.objects.annotate(number=Count('entries')).order_by('-number').first()  # TODO Какой автор имеет наибольшее количество опубликованных статей?
        # max_count_entries = Author.objects.annotate(number_of_entrys='entrys').order.by(-'number_of_entrys').first()
        self.answer3 = None  # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        # Entry.objects.select_related('author').filter(Q(tags__name='Кино') | Q(tags__name='Музыка'))
        self.answer4 = Author.objects.filter(gender='ж').count()  # TODO Сколько авторов женского пола зарегистрировано в системе?
        # Author.objects.filter(gender='ж').count()
        self.answer5 = Author.objects.filter(status_rule=False).count()/Author.objects.count()*100  # TODO Какой процент авторов согласился с правилами при регистрации?
        # Author.objects.filter(status_rule=False).count()/Author.objects.count()*100
        self.answer6 = AuthorProfile.objects.select_related('author').filter(stage__range=(1, 5))  # TODO Какие авторы имеют стаж от 1 до 5 лет?
        # AuthorProfile.objects.select_related('author').filter(stage__range=(1, 5))
        max_old = Author.objects.aggregate(max_old=Max('age'))
        self.answer7 = Author.objects.filter(age=max_old['max_old'])   # TODO Какой автор имеет наибольший возраст?
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()  # TODO Сколько авторов указали свой номер телефона?
        self.answer9 = Author.objects.filter(age__lt=25)  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer10 = Entry.objects.values('author').annotate(count=Count('id'))  # TODO Сколько статей написано каждым автором?
        # Entry.objects.values('author').annotate(count=Count('id'))
        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)

