#!/usr/bin/env python3
"""
Main entry point for BaZi Calculator
"""

import sys
from BZPaipan import BzPaipan
from BzRules import Bzrules


def main():
    """Main function for the BaZi calculator application"""
    print("=== BaZi Calculator ===")
    print("Based on Shouxing Astronomical Calendar")
    print()
    
    # Create paipan instance
    paipan = BzPaipan()
    
    # Example calculation with default values (2002-12-25 08:00)
    print("Example calculation:")
    print("Date: 2002-12-25 08:00")
    
    try:
        # Get BaZi calculation
        bzyj = paipan.getPaipanbySun(2002, 12, 25, 8)
        bzyj.getPaiPan()
        
        print("\nResults:")
        print("Ten Gods Combination:", Bzrules.getTgHe(bzyj.tglist))
        print("Ten Gods Clash:", Bzrules.getTgChong(bzyj.tglist))
        print("Earthly Branches Combination:", Bzrules.getZhiHe(bzyj.zhilist))
        print("Earthly Branches Clash:", Bzrules.getZhiChong(bzyj.zhilist))
        
    except Exception as e:
        print(f"Error during calculation: {e}")
        return 1
    
    print("\nCalculation completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())