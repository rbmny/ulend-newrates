import pandas as pd

d = {'Rating': ['A1','A2','A3','A4','B1','B2','B3','B4','B5','B6','C1','C2','C3','C4','C5','D1','D2','D3','D4'],
'Score': [850,810,770,730,690,650,610,570,530,490,450,410,370,330,290,250,210,170,100],
 'Imovel 120%': [0.65,0.73,0.80,0.88,0.94,1.00,1.16,1.25,1.34,1.44,1.49,1.60,1.67,1.83,1.95,2.09,2.22,2.38,2.47],
  'Imovel 80%': [0.70,0.78,0.85,0.93,0.99,1.05,1.21,1.30,1.39,1.49,1.54,1.65,1.72,1.88,2.00,2.14,2.27,2.43,2.52],
   'Recebiveis 50%': [1.14,1.22,1.28,1.36,1.41,1.47,1.62,1.71,1.80,1.89,1.94,2.04,2.11,2.26,2.38,2.51,2.64,2.78,2.87],
    'Recebiveis 150%': [1.02,1.09,1.15,1.22,1.26,1.32,1.45,1.53,1.61,1.69,1.73,1.83,1.89,2.02,2.13,2.24,2.36,2.49,2.57],
     'Garantia 20%': [1.14,1.22,1.28,1.36,1.41,1.47,1.62,1.71,1.80,1.89,1.94,2.04,2.11,2.26,2.38,2.51,2.64,2.78,2.87],
      'Garantia 50%': [1.02,1.09,1.15,1.22,1.26,1.32,1.45,1.53,1.61,1.69,1.73,1.83,1.89,2.02,2.13,2.24,2.36,2.49,2.57],
       'Aval': [1.20,1.28,1.35,1.43,1.49,1.55,1.71,1.80,1.89,1.99,2.04,2.15,2.22,2.38,2.50,2.64,2.77,2.93,3.02]}

df = pd.DataFrame(data=d)

print(df)
