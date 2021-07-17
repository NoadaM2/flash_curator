var
  s: string;
  i: integer;
begin
  var buf:= new List<string>;
  s:=ReadAllText('F:\Downloads from Yandex and Chrome\24hardparty.txt');
  i := 1;
  while i <= (s.Length - 10) do
  begin  // Реализуем почти стандартный алгоритм проверки на ПСП(правильность скобочной последовательности)
    
    if s[i:(i + 5)] = 'Артем' then
    begin
      buf.add('Артем');
      i += 5;
    end;
    
    if s[i:(i + 6)] = 'Пьяный' then
    begin
      buf.add('Пьяный');
      i += 6;
    end;
    
    if s[i:(i + 4)] = 'Саня' then
    begin
      buf.add('Саня');
      i += 4;
    end;
    
    if s[i:(i + 4)] = 'Стас' then
    begin
      buf.add('Стас');
      i += 4;
    end;
    
    if s[i:(i + 4)] = 'Флэш' then
      begin
        if 'Артем' in buf then
          buf.remove('Артем')
        else 
            buf.add('Флэш');
        i += 4;
      end;
    
    if s[i:(i + 6)] = 'Мастер' then
      begin
        if 'Пьяный' in buf then
          buf.remove('Пьяный')
        else 
            buf.add('Мастер');
        i += 6;
      end;
    
    if s[i:(i + 5)] = 'Касио' then
      begin
        if 'Саня' in buf then
          buf.remove('Саня')
        else
            buf.add('Касио');
        i += 5;
      end;
    
    if s[i:(i + 10)] = 'Валентиныч' then
      begin
         if 'Стас' in buf then
          buf.remove('Стас')
      else 
          buf.add('Валентиныч');
      i += 10;
      end; 
  end;
  print(buf)
end.