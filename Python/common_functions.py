# common functions
import sys
import logging

def strip_code_comments(code, SQL_or_PY, Multi_or_Single, Exclude_or_Include, look_for_start, look_for_end=''):
    " Doc: Removes comments from in-line sql or python code "
    this_method="strip_code_comments"

    code = code
    temp_code = ''
    start_pos_init = 0
    start_pos = 0
    end_pos = 0
    NEW_LINE = '\n'

    look_for_end = NEW_LINE if look_for_end=='' else look_for_end

    if Multi_or_Single == 'M' and SQL_or_PY=='SQL':
        while(look_for_start in code or look_for_end in code):
            start_pos=(code.find(look_for_start, start_pos_init, len(code)))
            end_pos=(code.find(look_for_start, start_pos, len(code)))
            code=code[:start_pos]+code[end_pos+len(look_for_end)]
            if start_pos in (0, -1):
                break
    
    if Multi_or_Single=='S' and SQL_or_PY in ('SQL','PY'):
        if Exclude_or_Include=='E':
            for eachline in code.splitlines(True):
                start_pos=(eachline.find(look_for_start, start_pos_init, len(eachline)))
                temp_code=temp_code+eachline[:start_pos]+NEW_LINE
        else:
            start_pos=(code.find(look_for_start, start_pos_init, len(code)))
            end_pos=(code.find(look_for_end, start_pos+len(look_for_start), len(code)))
            temp_code=code[start_pos+len(look_for_start):end_pos]
        code=temp_code
    
    return code


def main():
    this_method="main"

    script="""
    --Test
    SELECT current_date;
    """

    print(f"{this_method}: input(SQL)>> ", script)
    r=strip_code_comments(script,'SQL','S','E','--')
    print(f"{this_method}: output(SQL)>> ", r)

    script="""
    #Test.py
    def test():
        print("Hello!")
    """

    print(f"{this_method}: input(Python)>> ", script)
    r=strip_code_comments(script,'PY','S','E','#')
    print(f"{this_method}: output(Python)>> ", r)


if __name__ == '__main__':
    main()
