from django.core.management.base import BaseCommand
from django.utils import timezone
from polls.models import Question, Choice
import datetime


class Command(BaseCommand):
    help = 'Loads sample poll data'

    def handle(self, *args, **kwargs):
        # Check if data already exists
        if Question.objects.exists():
            self.stdout.write(self.style.WARNING('Sample data already exists. Skipping...'))
            return

        # Create sample questions
        q1 = Question.objects.create(
            question_text="What's your favorite Convox feature?",
            pub_date=timezone.now() - datetime.timedelta(days=5)
        )
        
        Choice.objects.create(question=q1, choice_text='Easy deployments', votes=7)
        Choice.objects.create(question=q1, choice_text='Automatic SSL certificates', votes=5)
        Choice.objects.create(question=q1, choice_text='Simple scaling', votes=3)
        Choice.objects.create(question=q1, choice_text='Cloud Machines', votes=12)

        q2 = Question.objects.create(
            question_text="Which cloud provider do you prefer?",
            pub_date=timezone.now() - datetime.timedelta(days=2)
        )
        
        Choice.objects.create(question=q2, choice_text='AWS', votes=8)
        Choice.objects.create(question=q2, choice_text='Google Cloud', votes=4)
        Choice.objects.create(question=q2, choice_text='Azure', votes=2)
        Choice.objects.create(question=q2, choice_text='Convox Cloud (no cloud provider needed!)', votes=15)

        q3 = Question.objects.create(
            question_text="What's your preferred deployment frequency?",
            pub_date=timezone.now() - datetime.timedelta(hours=1)
        )
        
        Choice.objects.create(question=q3, choice_text='Multiple times per day', votes=10)
        Choice.objects.create(question=q3, choice_text='Daily', votes=6)
        Choice.objects.create(question=q3, choice_text='Weekly', votes=3)
        Choice.objects.create(question=q3, choice_text='Monthly', votes=1)

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {Question.objects.count()} questions with choices'))