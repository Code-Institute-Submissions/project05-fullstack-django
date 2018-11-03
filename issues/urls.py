from django.conf.urls import url
from issues.views import get_all_bugs, bug_detail, create_or_edit_bug, vote_bug,\
    get_all_features, feature_detail, create_or_edit_feature, vote_feature

urlpatterns = [
    url(r'^$', get_all_bugs, name='get_all_bugs'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/vote/$', vote_bug, name='vote_bug'),

    url(r'^all_features$', get_all_features, name='get_all_features'),
    url(r'^(?P<pk>\d+)/editfeature/$',
        create_or_edit_feature, name='edit_feature'),
    url(r'^(?P<pk>\d+)/features/$', feature_detail, name='feature_detail'),
    url(r'^newfeature/$', create_or_edit_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/votefeature/$', vote_feature, name='vote_feature'),

]
