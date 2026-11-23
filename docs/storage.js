// 공통 모듈: 모든 페이지가 같은 저장 키와 같은 기록 형식을 사용한다.
// 이 파일을 수정할 때는 팀원과 먼저 이슈로 상의한다.
//
// 기록 형식 (Python 콘솔 버전의 records와 동일)
// { date: "YYYY-MM-DD", exercise: "스쿼트", weight: 60, reps: 10, sets: 3 }

const STORAGE_KEY = "records";

function loadRecords() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    const data = raw ? JSON.parse(raw) : [];
    return Array.isArray(data) ? data : [];
  } catch (e) {
    return [];
  }
}

function saveRecords(records) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(records));
    return true;
  } catch (e) {
    return false;
  }
}

function addRecord(record) {
  const all = loadRecords();
  all.push(record);
  return saveRecords(all);
}

function clearRecords() {
  try {
    localStorage.removeItem(STORAGE_KEY);
  } catch (e) {
    /* 저장소를 못 쓰는 환경이면 무시 */
  }
}

// 로컬 시간 기준 YYYY-MM-DD (toISOString은 UTC라서 쓰지 않는다)
function dateString(d = new Date()) {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}

// 월요일~일요일 한 주의 범위
function getWeekRange(base = new Date()) {
  const d = new Date(base.getFullYear(), base.getMonth(), base.getDate());
  const diff = (d.getDay() + 6) % 7; // 월요일 = 0
  const start = new Date(d);
  start.setDate(d.getDate() - diff);
  const end = new Date(start);
  end.setDate(start.getDate() + 6);
  return { start: dateString(start), end: dateString(end), startDate: start };
}

// 화면에 글자를 넣을 때는 innerHTML 대신 이 함수를 쓴다 (입력값이 코드로 실행되는 것을 막는다)
function el(tag, text, className) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = text;
  if (className) node.className = className;
  return node;
}

function fmtNum(n) {
  return String(Math.round(Number(n) * 10) / 10);
}

// 같은 종목 기록 중 최고 무게 (무게가 같으면 먼저 입력한 기록)
function findBest(records) {
  let best = records[0];
  records.forEach((r) => {
    if (r.weight > best.weight) best = r;
  });
  return best;
}

// ====================================================================
// 기능별 구역: 담당자는 자기 구역 안에서만 코드를 추가한다.
// 구역 표시 줄은 지우지 않는다. 다른 구역은 수정하지 않는다.
// ====================================================================

// --- 기록 삭제 (윤성) ---
// (구현 예정)

// --- 주간 목표 (선후) ---
// (구현 예정)

// --- 예상 1RM (건우) ---
// 예상 1RM (Epley 공식: 무게 x (1 + 횟수/30)). 실제 측정값이 아니라 추정치다.
function estimate1RM(weight, reps) {
  const w = Number(weight);
  const r = Number(reps);
  if (!(w > 0) || !(r >= 1)) return 0;
  return r === 1 ? w : w * (1 + r / 30);
}

// --- 달력과 연속 운동일 (선후) ---
// (구현 예정)

// --- 기록 백업 (윤성) ---
// (구현 예정)

// --- 신기록 알림 (윤성) ---
// (구현 예정)

// --- 빠른 입력 (윤성) ---
// (구현 예정)

// --- 지난주 대비 (선후) ---
// (구현 예정)
