import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from authors.models import Authors, Book


# #level 1
# #Пример из документации
# #определяем поле "hello` без аргументов
# class Query(ObjectType):
#     #определяем поле "hello` без аргументов
#     hello = graphene.String(default_value="Hi!")
#
#
# schema = graphene.Schema(query=Query)

# level 2

# #1.Создали тип для описания Автора
# #2.DjangoObjectType = позволяет автоматически создать
# # нужные типы полей для указанной модели и указать нужные поля!!
# class AuthorType(DjangoObjectType):
#     class Meta:
#         model = Authors
#         fields = '__all__'
#
# #1.Определяем поле "all_authors` как список авторов
# # 2. resolve_all_authors отдает список авторов
# class Query(ObjectType):
#
#     all_authors = graphene.List(AuthorType)
#
#     def resolve_all_authors(root,info):
#         return Authors.objects.all()
#
# schema = graphene.Schema(query=Query)


# #level 3
#
# #1.Создали тип для описания Автора
# #2.DjangoObjectType = позволяет автоматически создать
# # нужные типы полей для указанной модели и указать нужные поля!!
# class AuthorType(DjangoObjectType):
#     class Meta:
#         model = Authors
#         fields = '__all__'
#
# #1.Создали тип для описания Книг
# #2.DjangoObjectType = позволяет автоматически создать
# # нужные типы полей для указанной модели и указать нужные поля!!
# class BookType(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
# #1.Определяем поле "all_authors` как список авторов
# #2.Определяем поле "all_book` как список книг
# #3. resolve_all_authors отдает список авторов
# #3. resolve_all_book отдает список книг
# class Query(ObjectType):
#
#     all_authors = graphene.List(AuthorType)
#     all_book = graphene.List(BookType)
#
#     def resolve_all_authors(root,info):
#         return Authors.objects.all()
#
#     def resolve_all_book(root,info):
#         return Book.objects.all()
#
# schema = graphene.Schema(query=Query)


# level 4 Запросы с параметрами

# # 1.Создали тип для описания Автора
# # 2.DjangoObjectType = позволяет автоматически создать
# # нужные типы полей для указанной модели и указать нужные поля!!
# class AuthorType(DjangoObjectType):
#     class Meta:
#         model = Authors
#         fields = '__all__'
#
#
# # 1.Создали тип для описания Книг
# # 2.DjangoObjectType = позволяет автоматически создать
# # нужные типы полей для указанной модели и указать нужные поля!!
# class BookType(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#
# # 1.Определяем поле "author_by_id` Поле и указывает тип int заполнения обязательно
# # 2. resolve_author_by_id отдает список всех авторов если нет параметра
# # иначе отдает конретного автора
# class Query(ObjectType):
#     author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))
#
#     def resolve_author_by_id(root, info, id=None):
#         if id:
#             return Authors.objects.get(id=id)
#         return Authors.objects.all()
#
#     # # УСЛОЖНЯЕМ
#     # 1.Определяем поле "books_by_author` как список книг ставим не обязательным
#     # 2. resolve_books_by_author отдает с фильтрацией по first_name
#
#     books_by_author = graphene.List(BookType, first_name=graphene.String(required=False))
#     def resolve_books_by_author(self, info, first_name=None):
#         books = Book.objects.all()
#         if first_name:
#             books = books.filter(author__first_name=first_name)
#         return books
#
#
# schema = graphene.Schema(query=Query)



# level 5 Изменения данных

# 1.Создали тип для описания Автора
# 2.DjangoObjectType = позволяет автоматически создать
# нужные типы полей для указанной модели и указать нужные поля!!
class AuthorType(DjangoObjectType):
    class Meta:
        model = Authors
        fields = '__all__'


# 1.Создали тип для описания Книг
# 2.DjangoObjectType = позволяет автоматически создать
# нужные типы полей для указанной модели и указать нужные поля!!
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


# 1.Определяем поле "author_by_id` КАК Поле и указывает тип  ID  заполнения обязательно
# 2. resolve_author_by_id отдает список всех авторов если нет параметра
# иначе отдает конретного автора
class Query(ObjectType):
    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))

    def resolve_author_by_id(root, info, id=None):
        if id:
            return Authors.objects.get(id=id)
        return Authors.objects.all()

    # # УСЛОЖНЯЕМ
    # 1.Определяем поле "books_by_author` как список книг ставим не обязательным
    # 2. resolve_books_by_author отдает с фильтрацией по first_name
    books_by_author = graphene.List(BookType, first_name=graphene.String(required=False))

    def resolve_books_by_author(self, info, first_name=None):
        books = Book.objects.all()
        if first_name:
            books = books.filter(authors__first_name=first_name)
        return books


#Любое изменнеие это мутация
class AuthorUpdateMutation(graphene.Mutation):
    #Класс для передачи параметров
    class Arguments:
        birthday_year = graphene.Int(required=True)
        id = graphene.ID()

    # author будет содержать итоговый объект после изменения.
    author = graphene.Field(AuthorType)

    # Логика изменения
    @classmethod
    def mutate(self,root,info,birthday_year,id):
        author = Authors.objects.get(id=id)
        author.birthday_year = birthday_year
        author.save()
        # Возвращаем объект мутации с измеененным автором
        return AuthorUpdateMutation(author=author)

#Любое изменнеие это мутация
class AuthorCreateMutation(graphene.Mutation):
    # Класс для передачи параметров
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        birthday_year = graphene.Int(required=True)

    #author будет содержать итоговый объект после изменения.
    author = graphene.Field(AuthorType)

    #Логика изменения
    @classmethod
    def mutate(cls, root, info, first_name, last_name, birthday_year):
        author = Authors(first_name=first_name, last_name=last_name, birthday_year=birthday_year)
        author.save()
        #Возвращаем объект мутации с созданным автором
        return AuthorCreateMutation(author=author)

#Любое изменнеие это мутация
class AuthorDeleteMutation(graphene.Mutation):
    #Класс для передачи параметров
    class Arguments:
        id = graphene.ID()

    # author будет содержать итоговый объект после изменения.
    author = graphene.Field(AuthorType)

    # Логика изменения
    @classmethod
    def mutate(self,root,info,id):
        author = Authors.objects.get(id=id).delete()
        # Возвращаем объект мутации с измеененным автором
        return AuthorDeleteMutation(author=author)

#Объект для нескольких мутаций (нужно передать в схему)
class Mutations(graphene.ObjectType):
    update_author = AuthorUpdateMutation.Field()
    create_author = AuthorCreateMutation.Field()
    delete_author = AuthorDeleteMutation.Field()

schema = graphene.Schema(query=Query,mutation=Mutations)