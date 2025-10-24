import pytest
from playwright.sync_api import Page, expect

# Базовый URL, чтобы не повторять его
BASE_URL = 'https://effective-mobile.ru/'


@pytest.fixture(scope="function", autouse=True)
def auto_goto(page: Page):
    """
    Эта фикстура будет автоматически выполняться перед каждым тестом,
    открывая базовую страницу.
    """
    page.goto(BASE_URL)


# ---
# Здесь мы определяем все наши тестовые случаи.
# Каждый кортеж - это: (Имя ссылки, Ожидаемый хэш URL)
# ---
NAV_TEST_CASES = [
    ('О нас', '#about'),
    ('Услуги', '#moreinfo'),
    ('Проекты', '#cases'),
    ('Отзывы', '#Reviews'),  # Внимание: 'Reviews' с большой буквы, как в вашем тесте
    ('Контакты', '#contacts'),
    ('Выбрать специалиста', '#specialists')
]


@pytest.mark.parametrize("link_name, expected_fragment", NAV_TEST_CASES)
def test_header_navigation(page: Page, link_name: str, expected_fragment: str):
    """
    Единый тест для проверки всех ссылок в шапке сайта.
    Он будет запущен 6 раз - по одному разу для каждой пары
    данных из списка NAV_TEST_CASES.
    """

    # 1. Находим ссылку по ее имени (тексту) и кликаем
    page.get_by_role('link', name=link_name).click()

    # 2. Проверяем, что URL соответствует ожидаемому
    # Playwright сам подождет, пока URL не изменится
    expected_url = BASE_URL + expected_fragment
    expect(page).to_have_url(expected_url)

    # Паузы page.wait_for_timeout() удалены, так как они не нужны
    # и замедляют выполнение тестов.