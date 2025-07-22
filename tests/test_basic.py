#!/usr/bin/env python3
"""
Basic tests for BaZi Calculator
"""

import unittest
import sys
import os

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from BZPaipan import BzPaipan
from BzRules import Bzrules


class TestBaZiCalculator(unittest.TestCase):
    """Test cases for BaZi Calculator basic functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.paipan = BzPaipan()
    
    def test_paipan_instance_creation(self):
        """Test that BzPaipan instance can be created"""
        self.assertIsNotNone(self.paipan)
        self.assertIsInstance(self.paipan, BzPaipan)
    
    def test_basic_calculation(self):
        """Test basic BaZi calculation"""
        try:
            # Test with known date
            bzyj = self.paipan.getPaipanbySun(2002, 12, 25, 8)
            self.assertIsNotNone(bzyj)
            
            # Call getPaiPan method
            bzyj.getPaiPan()
            
            # Check that tglist and zhilist exist
            self.assertTrue(hasattr(bzyj, 'tglist'))
            self.assertTrue(hasattr(bzyj, 'zhilist'))
            
        except Exception as e:
            self.fail(f"Basic calculation failed: {e}")
    
    def test_rules_methods_exist(self):
        """Test that Bzrules methods exist and are callable"""
        # Create a test calculation
        bzyj = self.paipan.getPaipanbySun(2002, 12, 25, 8)
        bzyj.getPaiPan()
        
        # Test that rules methods exist and can be called
        try:
            result1 = Bzrules.getTgHe(bzyj.tglist)
            result2 = Bzrules.getTgChong(bzyj.tglist)
            result3 = Bzrules.getZhiHe(bzyj.zhilist)
            result4 = Bzrules.getZhiChong(bzyj.zhilist)
            
            # Results should not be None (though they might be empty lists)
            self.assertIsNotNone(result1)
            self.assertIsNotNone(result2)
            self.assertIsNotNone(result3)
            self.assertIsNotNone(result4)
            
        except Exception as e:
            self.fail(f"Rules calculation failed: {e}")


if __name__ == '__main__':
    unittest.main()