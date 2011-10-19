#!/usr/bin/python

APPNAME = 'regression'
VERSION = '0.1.0'

top = '.'
out = 'build'

def options(opt):
    opt.tool_options('compiler_cxx')

def configure(conf):
    conf.check_tool('compiler_cxx')
    conf.env.append_unique('CXXFLAGS', ['-std=c++0x', '-O2', '-W', '-Wall'])
    conf.env.append_unique('LINKFLAGS', ['-std=c++0x', '-O2', '-W', '-Wall'])
    conf.env.HPREFIX=conf.env.PREFIX + '/include/regression'

def build(bld):
    bld.SRCPATH=bld.path.abspath()+'/src'
    bld.recurse('src')
