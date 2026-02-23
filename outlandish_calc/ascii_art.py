SMALL_RESULT = """
[ RESULT ]
"""

MEDIUM_RESULT = """
*****************
*    RESULT     *
*****************
"""

BIG_RESULT = """
#########################
#                       #
#      MEGA RESULT      #
#                       #
#########################
"""

EXPLOSION = """
      _ ._  _ , _ ._
    (_ ' ( `  )_  .__)
  ( (  (    )   `)  ) _)
 (__ (_   (_ . _) _) ,__)
     `~~`\\ ' . /`~~`
          ;   ;
          /   \\
_________/_ __ \\_________
"""

PLUS_ART = """
  |  
--+--
  |  
"""

MINUS_ART = """
-----
"""

MULT_ART = """
 \\ / 
  X  
 / \\ 
"""

DIV_ART = """
  /  
 /   
/    
"""

def get_result_banner(drama_level: int) -> str:
    """
    Returns a result banner based on the drama level.
    
    Levels 1-2: SMALL_RESULT
    Levels 3-4: MEDIUM_RESULT
    Level 5+: BIG_RESULT
    """
    if drama_level <= 2:
        return SMALL_RESULT
    elif drama_level <= 4:
        return MEDIUM_RESULT
    else:
        return BIG_RESULT

def get_operation_art(operation: str) -> str:
    """
    Returns unique ASCII art for the specified operation.
    Supports +, -, *, /.
    """
    mapping = {
        '+': PLUS_ART,
        '-': MINUS_ART,
        '*': MULT_ART,
        '/': DIV_ART
    }
    return mapping.get(operation, "")