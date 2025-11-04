##здесь будет код
    def is_birthdate_near(self) -> bool:
        today = date.today()

        if self.birthdate:

            # Нормализуем дату рождения к текущему году
            try:
                birthday_this_year = self.birthdate.date().replace(year=today.year)
            except ValueError:
                # Обработка 29 февраля в невисокосный год
                birthday_this_year = self.birthdate.date().replace(year=today.year, day=28)

            days_until = abs((birthday_this_year - today).days)

            if days_until <= 3:
                return True
                
        return False