import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_filebeat_package(Package):
    filebeat = Package('filebeat')
    assert filebeat.is_installed
    assert filebeat.version.startswith("5.4")


def test_filebeat_run_and_enabled(Service, SystemInfo):
    filebeat = Service('filebeat')
    assert filebeat.is_running
    assert filebeat.is_enabled
