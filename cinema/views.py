from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Actor,
    Genre,
    CinemaHall,
    Movie,
    MovieSession
)
from cinema.serializers import ActorSerializer, GenreSerializer, \
    CinemaHallSerializer, MovieSerializer, MovieSessionSerializer, \
    MovieListSerializer, MovieRetrieveSerializer, MovieSessionListSerializer, \
    MovieSessionRetrieveSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        if self.action in ["list", "retrieve"]:
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(ModelViewSet):
    def get_queryset(self):
        queryset = MovieSession.objects.all()
        if self.action in ["list", "retrieve"]:
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer
