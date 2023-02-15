import validation, validators, ipaddress

class Validation:

    @staticmethod
    def validate_ip(ip):
        parts = ip.split('.')
        return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private

    @staticmethod
    def validate_port(port, rand=False):
        """ validate port number """
        if rand:
            return port.isdigit() and int(port) >= 0 and int(port) <= 65535
        else:
            return port.isdigit() and int(port) >= 1 and int(port) <= 65535

    @staticmethod
    def validate_time(time):
        """ validate attack duration """
        return time.isdigit() and int(time) >= 10 and int(time) <= 14400

    @staticmethod
    def validate_size(size):
        """ validate buffer size """
        return size.isdigit() and int(size) > 1 and int(size) <= 65500

    @staticmethod
    def validate_domain(domain):
        return validators.domain(domain)

    @staticmethod
    def validate_url(url):
        return validators.url(url)