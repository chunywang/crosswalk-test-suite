#!/usr/bin/env python
#
# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Hongjuan, Wang<hongjuanx.wang@intel.com>

import unittest
import os, sys, commands, filecmp
import comm

class TestPackertoolsFunctions(unittest.TestCase):
  def test_compressor_minify(self):
      comm.clear_compressor()
      compre = " --compressor"
      comm.compressor(compre, self)
      self.assertFalse(filecmp.cmp(comm.compDir + "script.js", comm.oriDir + "script.js"))
      self.assertFalse(filecmp.cmp(comm.compDir + "style.css", comm.oriDir + "style.css"))
      compscript = os.path.getsize(comm.compDir + "script.js")
      oriscript = os.path.getsize(comm.oriDir + "script.js")
      compstyle = os.path.getsize(comm.compDir + "style.css")
      oristyle = os.path.getsize(comm.oriDir + "style.css")
      self.assertTrue((oriscript > compscript))
      self.assertTrue((oristyle > compstyle))
      comm.clear_compressor()

  def test_compressor_minifycss(self):
      comm.clear_compressor()
      compre = " --compressor=css"
      comm.compressor(compre, self)
      self.assertTrue(filecmp.cmp(comm.compDir + "script.js", comm.oriDir + "script.js"))
      self.assertFalse(filecmp.cmp(comm.compDir + "style.css", comm.oriDir + "style.css"))
      compstyle = os.path.getsize(comm.compDir + "style.css")
      oristyle = os.path.getsize(comm.oriDir + "style.css")
      self.assertTrue((oristyle > compstyle))
      comm.clear_compressor()

  def test_compressor_minifyjs(self):
      comm.clear_compressor()
      compre = " --compressor=js"
      comm.compressor(compre, self)
      self.assertFalse(filecmp.cmp(comm.compDir + "script.js", comm.oriDir + "script.js"))
      self.assertTrue(filecmp.cmp(comm.compDir + "style.css", comm.oriDir + "style.css"))
      compscript = os.path.getsize(comm.compDir + "script.js")
      oriscript = os.path.getsize(comm.oriDir + "script.js")
      self.assertTrue((oriscript > compscript))
      comm.clear_compressor()

  def test_compressor_nominify(self):
      comm.clear_compressor()
      compre = ""
      comm.compressor(compre, self)
      self.assertTrue(filecmp.cmp(comm.compDir + "script.js", comm.oriDir + "script.js"))
      self.assertTrue(filecmp.cmp(comm.compDir + "style.css", comm.oriDir + "style.css"))
      comm.clear_compressor()

if __name__ == '__main__':  
    unittest.main()
