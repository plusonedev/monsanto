from django.db import models
import hashlib, time

class PreseedInstance(models.Model):
    VERSIONS = [('stretch','STRETCH')]
    NETWORK_TYPES = [('dhcp','DHCP'),('static','STATIC')]
    
    instance_id = models.CharField(max_length = 100, editable = False)
    
    version = models.CharField(
        max_length = 12,
        choices = VERSIONS,
        default = 'stretch',
    )
    
    network_type = models.CharField(
        max_length = 6,
        choices = NETWORK_TYPES,
        default = 'static',
    )
    
    ip_address = models.CharField(max_length = 15)
    mask = models.CharField(max_length = 15)
    gateway = models.CharField(max_length = 15)
    nameserver = models.CharField(max_length = 100)
    
    hostname = models.CharField(max_length = 100)
    domain = models.CharField(max_length = 100)
    ntp_server = models.CharField(max_length = 100, default = "pool.ntp.org")
    
    root_password = models.CharField(max_length = 100, blank = True, default = "")
    
    fullname = models.CharField(max_length = 100, default = "")
    username = models.CharField(max_length = 100, default = "")
    user_password = models.CharField(max_length = 100, default = "")
    user_ssh_key = models.TextField(default = "")
    apps = models.TextField(default = "", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
       
    def __str__(self):
        return self.instance_id.upper()
    
    def save(self, *args, **kwargs):
        source_string = self.ip_address + self.version + self.network_type + str(time.time())
        hash_object = hashlib.sha256(source_string.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        self.instance_id = hex_dig[0:6].upper()
        
        super(PreseedInstance, self).save(*args, **kwargs)
