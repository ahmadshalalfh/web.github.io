# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [

        (T('courses_schedules'), False, URL('course', 'schedules'), []),
        (T('courses'), False, URL('course', 'courses'), []),
         (T('studentschedules'), False, URL('course', 'studentschedules'), []),
        (T('studentcourses'), False, URL('course', 'studentcourses'), [])


    ]

