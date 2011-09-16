# Created On: 2011/09/16
# Copyright 2011 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from hscommon.trans import tr

from core.prioritize import (KindCategory, FolderCategory, FilenameCategory, NumericalCategory,
    SizeCategory, MtimeCategory)

class DurationCategory(NumericalCategory):
    NAME = tr("Duration")
    
    def extract_value(self, dupe):
        return dupe.duration

class BitrateCategory(NumericalCategory):
    NAME = tr("Bitrate")
    
    def extract_value(self, dupe):
        return dupe.bitrate

class SamplerateCategory(NumericalCategory):
    NAME = tr("Samplerate")
    
    def extract_value(self, dupe):
        return dupe.samplerate

def all_categories():
    return [KindCategory, FolderCategory, FilenameCategory, SizeCategory, DurationCategory,
        BitrateCategory, SamplerateCategory, MtimeCategory]
