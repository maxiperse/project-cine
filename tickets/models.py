from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    poster_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showtime = models.DateTimeField()
    available_seats = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.movie.title} - {self.showtime.strftime('%Y-%m-%d %H:%M')}"

class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    num_tickets = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva para {self.customer_name} - {self.showtime.movie.title}"