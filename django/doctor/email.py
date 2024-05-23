from django.core.mail.backends.smtp import EmailBackend
import ssl
''''
class SSLEmailBackend(Email):
    def _get_ssl_context(self):
        context = ssl.create_default_context()
        context.load_cert_chain(certfile=settings.EMAIL_CERTFILE, keyfile=settings.EMAIL_KEYFILE)
        return context

    def open(self):
        if self.connection:
            return False
        try:
            self.connection = self.connection_class(self.host, self.port, **self.connection_params)
            self.connection.ehlo()
            ssl_context = self._get_ssl_context()
            self.connection.starttls(context=ssl_context)
            self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except Exception:
            if not self.fail_silently:
                raise
            return False '''