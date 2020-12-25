from django.test import TestCase
from budget.models import Project, Category, Expense


class TestViews(TestCase):

    def setUp(self):
        self.project1 = Project.objects.create(
            name='project 1',
            budget=10000
        )
        self.category1 = Category.objects.create(
            project=self.project1,
            name='category1'
        )
        self.expense1 = Expense.objects.create(
            project=self.project1,
            title="expense1",
            amount=1000,
            category=self.category1
        )

    def test_project_slug_is_assigned_on_creation(self):
        self.assertEquals(self.project1.slug, 'project-1')

    def test_project_budget_left(self):
        self.assertEquals(self.project1.budget_left, 9000)

    def test_project_total_transactions(self):
        self.assertEquals(self.project1.total_transactions, 1)
