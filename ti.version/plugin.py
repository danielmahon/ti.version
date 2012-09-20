#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# example compiler plugin
# the config object is a set of properties
# that are passed (dependent on platform)
# that will allow you to hook into the compiler tooling
# 
 
import os
import json
 
def compile(config):
    print "[INFO] Compiler plugin: ti.version loaded and working for %s" % config['platform']
 
    project_dir = config['project_dir']
    resource_dir = os.path.abspath(os.path.join(project_dir, 'Resources'))
 
    version_file = os.path.join(resource_dir, 'package.json')
 
    if os.path.exists(version_file):
        vf = open(version_file, 'r').read()
 
        try:
            data = json.loads(vf)
    
            _oldVersion = data["version"]
            _version = data["version"].split(".")
            _major = _version[0]
            _minor = _version[1]
            _patch = _version[2].split("-")[0]
            _build = _version[2].split("-")[1]
            
            # increment build number
            _build = int(_build) + 1
            
            # reconstruct json
            data["version"] = str(_major) + '.' + str(_minor) + '.' + str(_patch) + '-' + str(_build)
            
            print "[INFO] [ti.version]",_oldVersion,"->",data["version"]
    
        except:
            print "[ERROR] Invalid package.json file. Version number unable to auto-increment."
    
    else:
        print "[ERROR] No package.json file found in Resources. Creating a new one..."
        data = {"name": "new-application", "version": "0.0.1-0"}

    # write changes back to file
    vf = open(version_file, "w")
    vf.write(json.dumps(data, sort_keys=True, indent=2))
    vf.close()
