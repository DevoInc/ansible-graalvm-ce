ansible-graalvm-ce
=========

Installs graalvm community edition in CentOS 7, Ubuntu 16.04 and Ubuntu 18.04

Requirements
------------

None

Role Variables
--------------

graalvm_ce_version: can be set to either `latest` or a fixed version. Defaults to `latest`.

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansible-graalvm-ce, graalvm_ce_version: 19.1.1 }

License
-------

MIT