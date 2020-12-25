from django.test import SimpleTestCase
from budget.forms import ExpenseForm


class TestForms(SimpleTestCase):

    def test_expense_form_valid_data(self):
        form = ExpenseForm({
            'title': 'expense1',
            'amount': 1000,
            'category': 'category1'
        })

        self.assertTrue(form.is_valid())

    def test_expense_form_invalid_data(self):
        form = ExpenseForm({})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
