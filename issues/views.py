from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bug
from .forms import BugForm

# Create your views here.


def get_all_bugs(request):
    """
    Create a view taht will return a list
    of Bugs that were published prior to 'now'
    and render them to the bugs.html template
    """
    bugs = Bug.objects.filter(published_date__lte=timezone.now
                              ()).order_by('-published_date')
    return render(request, "bugs.html", {'bugs': bugs})


def bug_detail(request, pk):
    """
    Create a view that returns a single
    Bug object based on the bug ID (pk) and
    render it to the bugdetail.html template
    or return a 404 error if bug is not found
    """

    bug = get_object_or_404(Bug, pk=pk)
    print("Bug Detail", bug)
    print("Bug Detail PK", pk)
    bug.votes += 1
    bug.save()
    return render(request, "bugdetail.html", {'bug': bug})


def create_or_edit_bug(request, pk=None):
    """
    Create a view that allows us to create
    or edit a bug depending if the Bug ID
    is null or not
    """

    bug = get_object_or_404(Bug, pk=pk) if pk else None
    print("Bug EDIT", bug)
    print("Bug EDIT", pk)
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            bug = form.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugform.html', {'form': form})
