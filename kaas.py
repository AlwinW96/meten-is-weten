#Alwin Wezenbeek 99060433

vraag_geel = input('is de kaas geel? ')

if vraag_geel == 'y' and 'Y':
    vraag_gaten = (input('zitten er gaten in? '))
    if vraag_gaten == 'y' and 'Y':
        vraag_duur = (input('is de kaas belachelijk duur? '))
        if vraag_duur == 'y' and 'Y':
            print('Emmenthaler')
        else:
            print('Leerdammer')
    else:
        vraag_hard = (input('is de kaas hard als steen? '))
        if vraag_hard == 'y' and 'Y':
            print('Pammigiano Reggiano')
        else:
            print('Goudse kaas')

else:
    vraag_schimmels = (input('heeft de kaas blauwe schimmels? '))
    if vraag_schimmels == 'y' and 'Y':
        vraag_korst = (input('heeft de kaas een korst? '))
        if vraag_korst == 'y' and 'Y':
            print('Blue de Rochbaron')
        else:
            print('''foumme d'ambert''')
    else:
        vraag_korst2 = (input('heeft de kaas een korst? '))
        if vraag_korst2 == 'y' and 'Y':
            print('Camembert')
        else:
            print('Mozzarella')



