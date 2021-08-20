from Finance.models import User,Transaction
from Finance.forms import TransactionForm, UserForm
from django.shortcuts import render,redirect
from django.forms.formsets import formset_factory

# Create your views here.
def add_transaction(request):
    TransactionFormSet = formset_factory(TransactionForm, extra = 10, min_num=1, validate_min = True)
    if(request.method == 'POST'):
        user_form = UserForm(request.POST)
        transaction_formset = TransactionForm(request.POST)
        if all([user_form.is_valid() , transaction_formset.is_valid()]):
            user = user_form.save()
            for inline_form in transaction_formset:
                if inline_form.cleaned_data:
                    transaction = inline_form.save(commit=False)
                    transaction.user_id = user
                    transaction.save()
            return render(request,'Finance/index.html', {})
        else:
            user_form = UserForm()
            transaction_formset = TransactionForm()
        return render(request,'Finance/add_transaction.html', {
            'user_form':user_form,
            'transaction_form': transaction_formset,
        })

def add_users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = UserForm()
        return render(request, 'Finance/index.html', {
            'form': form
        })




def show_users(request):
    users = User.objects.all()
    return render(request, 'Finance/show.html', {
        'user' : users
    })

def show_transaction(request):
    transaction = Transaction.objects.all()
    return render(request, 'Finance/show.html', {
        'transaction' : transaction
    })

def edit_transaction(request):
    edit_trans = Transaction.objects.get(id=id)
    return render(request,'Finance/edit.html',{
        'edit_transaction':edit_trans
    })


def edit_users(request):
    edit_user = User.objects.get(id=id)
    return render(request,'Finance/edit.html',{
        'edit_users':edit_user
    })

def delete_transaction(request):
    del_trans = Transaction.objects.get(id = id)
    del_trans.delete()
    return redirect('Finance/show')


def delete_users(request):
    del_user = User.objects.get(id = id)
    del_user.delete()
    return redirect('Finance/show')

