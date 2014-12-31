"""Debug Plugin for EasyEngine."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook


def debug_plugin_hook(app):
    # do something with the ``app`` object here.
    pass


class EEDebugController(CementBaseController):
    class Meta:
        label = 'debug'
        description = 'debug command enables/disbaled stack debug'
        stacked_on = 'base'
        stacked_type = 'nested'
        arguments = [
            (['--stop'],
                dict(help='Stop debug', action='store_true')),
            (['--start'],
                dict(help='Start debug', action='store_true')),
            (['--nginx'],
                dict(help='Debug Nginx', action='store_true')),
            (['--php'],
                dict(help='Debug PHP', action='store_true')),
            (['--fpm'],
                dict(help='Debug FastCGI', action='store_true')),
            (['--mysql'],
                dict(help='Debug MySQL', action='store_true')),
            (['--wp'],
                dict(help='Debug WordPress sites', action='store_true')),
            (['--rewrite'],
                dict(help='Debug Nginx rewrite rules', action='store_true')),
            (['-i', '--interactive'],
                dict(help='Interactive debug', action='store_true')),
            ]

    @expose(hide=True)
    def debug_nginx(self):
        if self.start:
            print("Start Nginx debug")
            debug_address = (self.app.config.get('stack', 'ip-address')
                             .split())
            print(debug_address)
        else:
            print("Stop Nginx debug")

    @expose(hide=True)
    def debug_php(self):
        if self.start:
            print("Start PHP debug")
        else:
            print("Stop PHP debug")

    @expose(hide=True)
    def debug_fpm(self):
        if self.start:
            print("Start FPM debug")
        else:
            print("Stop FPM debug")

    @expose(hide=True)
    def debug_mysql(self):
        if self.start:
            print("Start MySQL debug")
        else:
            print("Stop MySQL debug")

    @expose(hide=True)
    def debug_wp(self):
        if self.start:
            print("Start WP debug")
        else:
            print("Stop WP debug")

    @expose(hide=True)
    def debug_rewrite(self):
        if self.start:
            print("Start WP-Rewrite debug")
        else:
            print("Stop WP-Rewrite debug")

    @expose(hide=True)
    def default(self):
        self.start = True
        self.interactive = False

        if self.app.pargs.stop:
            self.start = False

        if ((not self.app.pargs.nginx) and (not self.app.pargs.php)
           and (not self.app.pargs.fpm) and (not self.app.pargs.mysql)
           and (not self.app.pargs.wp) and (not self.app.pargs.rewrite)):
            self.debug_nginx()
            self.debug_php()
            self.debug_fpm()
            self.debug_mysql()
            self.debug_wp()
            self.debug_rewrite()

        if self.app.pargs.nginx:
            self.debug_nginx()
        if self.app.pargs.php:
            self.debug_php()
        if self.app.pargs.fpm:
            self.debug_fpm()
        if self.app.pargs.mysql:
            self.debug_mysql()
        if self.app.pargs.wp:
            self.debug_wp()
        if self.app.pargs.rewrite:
            self.debug_rewrite()

        if self.app.pargs.interactive:
            self.interactive = True


def load(app):
    # register the plugin class.. this only happens if the plugin is enabled
    handler.register(EEDebugController)
    # register a hook (function) to run after arguments are parsed.
    hook.register('post_argument_parsing', debug_plugin_hook)