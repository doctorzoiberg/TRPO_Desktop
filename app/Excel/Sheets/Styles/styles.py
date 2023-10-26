from openpyxl.styles import Font, Alignment, Border, Side


def title_font():
    sF = Font(name="TimesNewRoman",
              size=14,
              bold=True)
    return sF


def alignment():
    sA = Alignment(horizontal='center',
                   vertical='center')
    return sA


def border(side):
    sB = None
    if side == 'left':
        sB = Border(left=Side(border_style='thin',
                              color='00000000'))
    elif side == 'right':
        sB = Border(right=Side(border_style='thin',
                               color='00000000'))
    elif side == 'top':
        sB = Border(top=Side(border_style='thin',
                             color='00000000'))
    elif side == 'bottom':
        sB = Border(bottom=Side(border_style='thin',
                                color='00000000'))
    elif side == 'bottom-right':
        sB = Border(bottom=Side(border_style='thin',
                                color='00000000'),
                    right=Side(border_style='thin',
                               color='00000000'))
    elif side == 'left-bottom-right':
        sB = Border(left=Side(border_style='thin',
                              color='00000000'),
                    bottom=Side(border_style='thin',
                                color='00000000'),
                    right=Side(border_style='thin',
                               color='00000000'))
    elif side == 'all':
        sB = Border(left=Side(border_style='thin',
                              color='00000000'),
                    bottom=Side(border_style='thin',
                                color='00000000'),
                    right=Side(border_style='thin',
                               color='00000000'),
                    top=Side(border_style='thin',
                             color='00000000'))
    return sB
