# 로또 게임 TDD 구현 프로젝트

이 프로젝트는 next-step의 TDD, 클린 코드 with Java를 Python으로 바꿔 로또 게임을 구현한 Python 프로젝트입니다. 클린 코드 원칙을 준수하며 단계별로 기능을 확장했습니다.

## 프로젝트 개요

로또 게임을 TDD 방식으로 구현하며, 다음과 같은 단계로 진행했습니다:
- 1단계: 자동 로또 발급 기능 [lotto-ver1](https://github.com/ChaaaChaaa/tdd-lotto-python/tree/lotto-ver1)
- 2단계: 2등 추가 (보너스 볼) [lotto-ver2](https://github.com/ChaaaChaaa/tdd-lotto-python/tree/lotto-ver2)
- 3단계: 수동 로또 구매 기능 [lotto-ver3](https://github.com/ChaaaChaaa/tdd-lotto-python/tree/lotto-ver3)

## 테스트 전략 및 구현

### 테스트 시뮬레이션

전체 애플리케이션 흐름을 테스트하기 위한 통합 테스트를 구현했습니다:

- 사용자 입력 모킹을 통한 전체 시나리오 테스트
- 각 단계별 기능 검증:
  - 구입 금액 입력 및 검증
  - 수동/자동 티켓 구매 및 생성
  - 당첨 번호 및 보너스 번호 입력
  - 당첨 결과 및 수익률 계산

### 단위 테스트

주요 기능별 단위 테스트를 구현했습니다:

#### 티켓 관련 테스트
- 자동 티켓 생성 기능 테스트
- 랜덤 번호 생성 테스트
- 티켓 구매 로직 테스트

#### 당첨 확인 테스트
- 일반 당첨 케이스 테스트
- 보너스 번호 당첨 케이스 테스트
- 다양한 시나리오에 대한 당첨 결과 검증

#### 입출력 테스트
- 사용자 입력 처리 테스트
- 결과 출력 테스트

#### 유틸리티 테스트
- 수익률 계산 테스트
- 티켓 수량 계산 테스트

## 테스트 코드 구조

```
tests/
├── integration/
│   └── test_simulation.py - 전체 시뮬레이션 통합 테스트
├── lotto/
│   ├── test_rewards.py - 보상 시스템 테스트
│   └── test_winner_number.py - 당첨 번호 처리 테스트
├── script/
│   ├── test_input.py - 사용자 입력 처리 테스트
│   └── test_output.py - 결과 출력 테스트
├── ticket/
│   ├── test_random_number.py - 랜덤 번호 생성 테스트
│   ├── test_ticket.py - 티켓 생성 및 당첨 확인 테스트
│   └── test_ticket_shop.py - 티켓 구매 로직 테스트
└── utils/
    └── test_calculator.py - 수익률 계산 등 유틸리티 테스트
```

## 주요 테스트 기법

### 모킹(Mocking)

- `unittest.mock.patch`를 사용한 외부 의존성 모킹
- 사용자 입력(`builtins.input`) 모킹
- 랜덤 번호 생성 함수 모킹
- 출력 함수 모킹 및 호출 검증

### 테스트 케이스 설계

- 정상 케이스 테스트
- 경계값 테스트 (예: 구매 금액 경계값)
- 다양한 당첨 시나리오 테스트
- 예외 상황 테스트 (예: 0원 입력 시 ZeroDivisionError)

### 검증 기법

- 예상 결과와 실제 결과 비교 (`assertEqual`)
- 함수 호출 검증 (`assert_called_with`, `assert_has_calls`)
- 복잡한 데이터 구조 검증
- 예외 발생 검증 (`assertRaises`)

## 구현된 기능

- 로또 번호 자동 생성
- 수동 로또 번호 입력 및 검증
- 당첨 번호 및 보너스 번호 입력
- 당첨 결과 계산 및 통계
- 수익률 계산

## 프로젝트 구조

```
lotto/
├── src/
│   ├── lotto/
│   │   ├── rewards.py - 보상 시스템 (Enum 활용)
│   │   └── winner_number.py - 당첨 번호 처리
│   ├── script/
│   │   ├── input.py - 사용자 입력 처리
│   │   └── output.py - 결과 출력
│   ├── ticket/
│   │   ├── random_number.py - 랜덤 번호 생성
│   │   ├── ticket.py - 티켓 생성 및 당첨 확인
│   │   └── ticket_shop.py - 티켓 구매 로직
│   └── utils/
│       └── calculator.py - 수익률 계산 등 유틸리티
└── tests/ - 위에 설명된 테스트 구조
```


## 기술 스택

- Python 3.10
- unittest 프레임워크
- unittest.mock 모듈

## 개발 원칙

1. TDD 사이클 준수: 실패하는 테스트 작성 → 테스트 통과하는 코드 작성 → 리팩토링
2. 클린 코드 원칙 준수: 의미 있는 이름, 작은 함수, 단일 책임 원칙 등
3. SOLID 원칙 적용
4. 모킹을 통한 외부 의존성 제거
5. 테스트 가능한 코드 설계

## 테스트 실행 방법

```bash
# 모든 테스트 실행
python -m unittest discover tests

# 특정 테스트 파일 실행
python -m unittest tests.ticket.test_ticket
python -m unittest tests.integration.test_simulation
```
