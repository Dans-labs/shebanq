#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gluon.custom_import import track_changes; track_changes(True)

EXPIRE = 3600*24*30

@cache.action(time_expire=EXPIRE, cache_model=cache.ram, quick='VP')
def index():
    session.forget(response)
    response.title = T("SHEBANQ")
    response.subtitle = T("Query the Hebrew Bible through the ETCBC4 database")
    return response.render(dict())

@cache.action(time_expire=EXPIRE, cache_model=cache.ram, quick='VP')
def about():
    session.forget(response)
    response.title = T("SHEBANQ - about")
    response.subtitle = T("About the ETCBC4 database")
    return response.render(dict())

@cache.action(time_expire=EXPIRE, cache_model=cache.ram, quick='VP')
def help():
    session.forget(response)
    response.title = T("SHEBANQ - help")
    response.subtitle = T("Help for using SHEBANQ")
    return response.render(dict())

@cache.action(time_expire=EXPIRE, cache_model=cache.ram, quick='VP')
def sources():
    session.forget(response)
    response.title = T("SHEBANQ - sources")
    response.subtitle = T("Sources for recreating SHEBANQ")
    return response.render(dict())

@cache.action(time_expire=EXPIRE, cache_model=cache.ram, quick='VP')
def news():
    session.forget(response)
    response.title = T("SHEBANQ - news")
    response.subtitle = T("Release notes of SHEBANQ")
    return response.render(dict())

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """

    if not request.is_local: request.requires_https()
    response.title = T("User Profile")
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())


