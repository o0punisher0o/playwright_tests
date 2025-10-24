from playwright.sync_api import Page, expect


def test_about_us(page: Page):
    page.goto('https://effective-mobile.ru/')

    # О нас
    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)
    page.get_by_role('link', name='О нас').click()

    # Проверка, что URL страницы соответствует ожидаемому
    expect(page).to_have_url('https://effective-mobile.ru/#about')

    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)


def test_moreinfo(page: Page):
    page.goto('https://effective-mobile.ru/')

    # Услуги
    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)
    page.get_by_role('link', name='Услуги').click()

    # Проверка, что URL страницы соответствует ожидаемому
    expect(page).to_have_url('https://effective-mobile.ru/#moreinfo')

    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)


def test_cases(page: Page):
    page.goto('https://effective-mobile.ru/')

    # Услуги
    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)
    page.get_by_role('link', name='Проекты').click()

    # Проверка, что URL страницы соответствует ожидаемому
    expect(page).to_have_url('https://effective-mobile.ru/#cases')

    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)


def test_reviews(page: Page):
    page.goto('https://effective-mobile.ru/')

    # Услуги
    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)
    page.get_by_role('link', name='Отзывы').click()

    # Проверка, что URL страницы соответствует ожидаемому
    expect(page).to_have_url('https://effective-mobile.ru/#Reviews')

    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)


def test_contacts(page: Page):
    page.goto('https://effective-mobile.ru/')

    # Услуги
    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)
    page.get_by_role('link', name='Контакты').click()

    # Проверка, что URL страницы соответствует ожидаемому
    expect(page).to_have_url('https://effective-mobile.ru/#contacts')

    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)


def test_specialists(page: Page):
    page.goto('https://effective-mobile.ru/')

    # Услуги
    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)
    page.get_by_role('link', name='Выбрать специалиста').click()

    # Проверка, что URL страницы соответствует ожидаемому
    expect(page).to_have_url('https://effective-mobile.ru/#specialists')

    # --- Добавляем задержку ---
    # Пауза на 3 секунды (1500 миллисекунд), чтобы увидеть результат
    page.wait_for_timeout(1500)


