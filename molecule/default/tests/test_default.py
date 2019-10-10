import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_java_version(host):
    ansible_vars = host.ansible.get_variables()
    graalvm_ce_version = ansible_vars.get('graalvm_ce_version')
    java_output = host.run('/opt/graalvm-ce/bin/java -version')
    assert str(graalvm_ce_version) in java_output.stderr
