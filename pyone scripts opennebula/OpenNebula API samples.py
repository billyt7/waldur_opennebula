import pyone

one = pyone.OneServer("http://5.254.20.106:2633/RPC2", session="oneadmin:BFGDETio2020")

#Get the name and id of all templates available
vm_template = one.templatepool.info(-1,-1,-1).VMTEMPLATE[0]
id = vm_template.get_ID()
name = vm_template.get_NAME()
print(id, name)

#Function test of initialising pyone server
def test(first, second):
    first = "http://5.254.20.106:2633/RPC2"
    second = "oneadmin:BFGDETio2020"
    one = pyone.OneServer(first, session=second)
    templateinfo = one.template.info(5, True)

#test("http://5.254.20.106:2633/RPC2", "oneadmin:BFGDETio2020")

#Get template information
templateinfo = one.template.info(5, True)
print (templateinfo.NAME, templateinfo.ID)
my_vm = one.vmpool.info(-1,-1,-1,-1).VM[0]
id = my_vm.get_ID()
name = my_vm.get_NAME()
template = my_vm.get_TEMPLATE()
print(id, name, template)

#Starting and suspending vm actions
one.vm.action('resume', 7)
one.vm.action('suspend', 2)

#VM templating
VM = {'TEMPLATE': {'CONTEXT': {'NETWORK': u'YES',
  'SSH_PUBLIC_KEY': u'$USER[SSH_PUBLIC_KEY]'},
  'CPU': u'2',
  'DISK': {'DEV_PREFIX': u'vd',
  'IMAGE': u',
  'IMAGE_UNAME': u'',
  'SIZE': u'10240'},
  'MEMORY': u'2048',
  'NAME': u'cdd847468ae4.debug.local',
  'NIC': {'NETWORK': u'', 'NETWORK_UNAME': u"'},
  'VCPU': u'2'}}

#Template information ordering
OrderedDict([('CPU', '1'), ('MEMORY', '768'), ('DISK', OrderedDict([('DISK_ID', '0'), ('DATASTORE', 'default'),
('DATASTORE_ID', '1'), ('IMAGE', 'VM01-Clone-disk-0'), ('IMAGE_ID', '1'), ('SIZE', '5120'), ('TYPE', 'FILE'),
('CLONE', 'NO'), ('CLONE_TARGET', 'SYSTEM'), ('LN_TARGET', 'SYSTEM'), ('DISK_SNAPSHOT_TOTAL_SIZE', '0')])),
('NIC', OrderedDict([('IP', '5.254.20.108'), ('MAC', '02:00:05:fe:14:6c'), ('NETWORK', 'public-01'), ('NETWORK_ID', '0'),
('NIC_ID', '0'), ('SECURITY_GROUPS', '0')])), ('GRAPHICS', OrderedDict([('LISTEN', '0.0.0.0'), ('PORT', '5907'), ('TYPE', 'VNC')]))])

#Allocating a template
one.template.allocate(
       {
         'TEMPLATE': {
           'NAME': 'test100',
           'MEMORY': '1024',
           'DISK': { 'IMAGE_ID': '314'},
           'DISK': { 'IMAGE_ID': '310'},
           'CPU' : '1',
           'VCPU' : '2'
         }
       })

#Allocating a template
one.template.allocate('''
  NAME="test100"
  MEMORY="1024"
  DISK=[ IMAGE_ID= "314"]
  DISK=[ IMAGE_ID= "310"]
  CPU="1"
  VCPU="2"
''')


#Sample api gets
#-------------------------------------------------------------------------
#vmPoolInfo = one.vmpool.info(-1,-1,-1,-1)
#vmList = vmPoolInfo.get_VM()
#for vm in vmList:
#    print(vm.NAME)
#-------------------------------------------------------------------------
#marketpool = one.marketpool.info()
#m0 = marketpool.MARKETPLACE[0]
#print("Markeplace name is " + m0.NAME)
#-------------------------------------------------------------------------
#vm_template = one.templatepool.info(-1, -1, -1).VMTEMPLATE[0]
#vmTemplateId = vm_template.get_ID()
#vmTemplateName = vm_template.get_NAME()
#vmTemplateMemory = vm_template.get_MEMORY()
#print(vmTemplateId)
#print(vmTemplateName)
#-------------------------------------------------------------------------
#host = one.hostpool.info().HOST[0]
#dict(host.TEMPLATE)
#print(host.TEMPLATE)