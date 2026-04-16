import random
from locust import HttpUser, task, constant


class AddUser(HttpUser):
    wait_time = constant(0.1)

    @task
    def add(self):
        a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        self.client.get(f"/add?a={a}&b={b}")
