# TRANSLATION_REPORT

## 概览

- 评审范围：`translation/output/` 下 11 个 YAML 文件，对照 `translation/input/` 原文与 `.agents/skills/translate-rule/references/` 下的规范、术语表、卡名表进行检查。
- YAML 解析：11/11 文件可以被 Ruby YAML 解析器读取。
- 重要说明：`09_abilities.yaml` 虽然“可解析”，但结构并不合格。经本地核验，原文顶层 `sections` 为 12 个，输出文件仅剩 8 个；另外原文中的 15 个 `new:` 标记在输出中全部丢失。这说明该文件存在错误缩进和字段丢失，已经影响文档语义。
- 总体结论：已确认存在问题的文件为 `01_game_concepts.yaml`、`04_game_zones.yaml`、`07_access_breach.yaml`、`08_card_manipulation.yaml`、`09_abilities.yaml`、`10_additional_rules.yaml`、`11_appendix_timing_structures.yaml`。`02_parts_of_a_card.yaml`、`03_card_types.yaml`、`05_turns.yaml`、`06_runs.yaml` 暂未发现明确问题，但不等于“完全无瑕”。

## 文件结论

| 文件 | 结论 | 备注 |
| --- | --- | --- |
| `01_game_concepts.yaml` | issues | 固定规则短语与术语残留英文 |
| `02_parts_of_a_card.yaml` | pass | 暂未发现明确问题 |
| `03_card_types.yaml` | pass | 暂未发现明确问题 |
| `04_game_zones.yaml` | issues | 正文中残留未本地化中央服务器术语 |
| `05_turns.yaml` | pass | 暂未发现明确问题 |
| `06_runs.yaml` | pass | 暂未发现明确问题 |
| `07_access_breach.yaml` | issues | 卡名映射错误，且部分生成标记丢失 |
| `08_card_manipulation.yaml` | issues | `{n}` / `{term:...}` 标记丢失，且大量卡名未按表本地化 |
| `09_abilities.yaml` | issues | 结构损坏、`new:` 丢失、存在漏译与术语不一致 |
| `10_additional_rules.yaml` | issues | 个别术语关系翻反，`Trace [N]` / `Dividends N` 未按规范本地化 |
| `11_appendix_timing_structures.yaml` | issues | 关键流程语义被改写，且术语不统一 |

## 已确认问题清单

1. 文件：`01_game_concepts.yaml`
   位置：`rule_cannot_precedence`，输出行 23
   原文：`If a rule or ability directs something to happen, but another effect states that it cannot happen, the "cannot" ability takes precedence.`
   译文：`如果某条规则或能力指示某事发生，但另1个效果表示它不能发生，则以“cannot”能力为准。`
   原因：固定规则短语 `cannot` 未本地化，违反了“逻辑连接词显式翻译”和术语统一要求。

2. 文件：`01_game_concepts.yaml`
   位置：`rule_if_able` / `rule_do_as_much_as_you_can`，输出行 25、27
   原文：`If an instruction includes the words "if able," ...` / `If an instruction does not include the words "if able," ...`
   译文：`如果某条指示包含“if able”字样...` / `如果某条指示不包含“if able”字样...`
   原因：固定模板 `if able` 直接保留英文，未按规范落地为中文规则表达。

3. 文件：`01_game_concepts.yaml`
   位置：`rule_counters_cards` / `rule_counter_token`，输出行 256、259
   原文：`{term:Counters} and {term:tokens} ...` / `The terms "counter" and "token" are interchangeable.`
   译文：`{term:Counters}和{term:tokens}...` / `“counter”和“token”这两个术语可以互换。`
   原因：术语本体仍保留英文，未与“指示物 / 标记”的中文术语体系一致。

4. 文件：`04_game_zones.yaml`
   位置：`rule_three_central_servers` / `rule_archives_discard_pile`，输出行 252、258
   原文：`Archives`
   译文：`Archives`
   原因：正文叙述中仍保留 `Archives` 原文。按规范，正文应使用“档案库”，仅在缩写式或代码式场景保留英文。

5. 文件：`07_access_breach.yaml`
   位置：输出行 138
   原文：`...because of {card:Otoroshi}'s ability.`
   译文：`...因 {card:小丑} 的能力...`
   原因：`localize_name.yaml` 中 `Otoroshi` 的标准译名是 `{card:惊怪}`；译文写成 `{card:小丑}`，会指向错误卡牌。

6. 文件：`07_access_breach.yaml`
   位置：输出行 123、156
   原文：`{n}It cannot become a candidate as long as accessing it remains prohibited.{/n}` / `{n}If the Runner chooses ...{/n}`
   译文：对应句子已译成中文，但 `{n}...{/n}` 标记消失
   原因：原文新增内容高亮语法被删除，违反“只翻译文本、不得改动原始特殊标记”的要求。

7. 文件：`07_access_breach.yaml`
   位置：输出行 83
   原文：`This number is called the {term:Random Access Limit}.`
   译文：`这个数值称为随机读取上限。`
   原因：译文去掉了 `{term:...}` 术语标记，导致生成语法丢失。

8. 文件：`08_card_manipulation.yaml`
   位置：输出行 12、29、390、396
   原文：`{term:rez}` / `{term:derez}` / `{term:search}` / `{term:find}`
   译文：`激活` / `关闭` / `搜寻` / `找到`
   原因：中文词义本身基本正确，但 `{term:...}` 语法标记被删掉，破坏了文档生成所需的格式信息。

9. 文件：`08_card_manipulation.yaml`
   位置：输出行 42、52、267
   原文：含 `{n}...{/n}` 的新增文本，以及 `only`
   译文：新增标记缺失，`only` 保留英文
   原因：该文件同时存在特殊标记丢失和普通规则词漏译，说明翻译时对原始 YAML 内嵌语法的保留不稳定。

10. 文件：`08_card_manipulation.yaml`
    位置：输出行 72、79、147、173、232、276、289、338、403、416、430 等
    原文：`{card:Harbinger}`、`{card:Cultivate}`、`{card:Ad Blitz}`、`{card:Near-Earth Hub}` 等
    译文：对应 `{card:...}` 仍保留英文卡名
    原因：这些卡名均能在 `localize_name.yaml` 中找到标准中文名，但输出未本地化，属于系统性术语表未落实。

11. 文件：`09_abilities.yaml`
    位置：输出行 118、879、916、983 一带；文件整体结构
    原文：原文件有 12 个顶层 `sections`
    译文：这些 section 头前多出两格缩进，解析后输出文件只剩 8 个顶层 `sections`
    原因：这不是单纯措辞问题，而是 YAML 结构损坏。文件虽然可解析，但多个顶层章节被错误覆盖，已经影响规则文档的真实结构。

12. 文件：`09_abilities.yaml`
    位置：全文件
    原文：输入文件中共保留 15 个 `new:` 标记
    译文：输出文件中 `new:` 字段数量为 0
    原因：翻译任务只应改动 `text`、`snippet`、`toc_entry`，删除 `new:` 会改变“新增内容高亮”的语义。

13. 文件：`09_abilities.yaml`
    位置：输出行 268、541、822、826
    原文：`Some abilities dictate a value for X...` / `The Runner encounters a piece of ice outside of a run...` / `The Runner accesses {card:Breached Dome}...` / `While the result of a successful trace from {card:Flare} is imminent...`
    译文：上述示例在输出中仍为英文原句，仅局部替换了卡名
    原因：这些都属于 `text` 字段正文，属于明确漏译。

14. 文件：`09_abilities.yaml`
    位置：输出行 19、278、280、1078-1087
    原文：`static ability` / `instruction` / `persistent`
    译文：`静态能力` / `指令` / `持续`
    原因：与参考术语不一致。评审中确认该文件系统性使用了与术语表不一致的译法，并且会与其他概念（如 `lingering effect -> 持续效果`）产生混淆。

15. 文件：`09_abilities.yaml`
    位置：输出行 32、688、690
    原文：`{card:Armand "Geist" Walker}` / `{card:Tsakhia "Bankhar" Gantulga}`
    译文：仍保留英文卡名
    原因：`localize_name.yaml` 已提供标准中文名，未本地化。

16. 文件：`10_additional_rules.yaml`
    位置：伤害章节（review 定位 `sections.3.rules.0.text`）
    原文：`The Runner {term:suffers} (sometimes referred to as "{term:takes}") damage ...`
    译文：`潜袭者会按照所指定伤害类型的规则承受（有时也称为“受到”）伤害...`
    原因：`suffer` 与 `take` 的对应关系被翻反了；这是术语层面的语义错误。

17. 文件：`10_additional_rules.yaml`
    位置：追踪章节（review 定位 `sections.7.rules.0.text; sections.7.rules.4.text`）
    原文：`"Trace [N]" ...`
    译文：`“Trace [N]”...`
    原因：规范要求统一写成 `<trace>追踪 X</trace>`，这里保留英文模板，不符合既定格式。

18. 文件：`10_additional_rules.yaml`
    位置：目标章节（review 定位 `sections.10.rules.1.rules.0.text`）
    原文：`designating 1 card from outside the game to represent each server`
    译文：`从移出游戏区选出1张卡牌分别代表1台服务器`
    原因：`outside the game` 被误译成了“移出游戏区”，且句意也从“一台服务器对应一张卡牌”变成了不自然的中文表达，属于含义偏差。

19. 文件：`10_additional_rules.yaml`
    位置：红利章节（review 定位 `sections.12.rules.0.text`）
    原文：`"Dividends N" means ...`
    译文：`“Dividends N”意为...`
    原因：关键字本体仍保留英文，未按“红利”体系本地化。

20. 文件：`11_appendix_timing_structures.yaml`
    位置：输出行 150
    原文：`If breaching HQ or R&D, determine how many accesses from Corp's hand or deck.`
    译文：`如果侵入总部或研发中心，则确定从公司的手牌或牌组中有多少张可读取卡牌。`
    原因：`accesses` 在这里表示“读取次数”，不是“当前有多少张可读取卡牌”。译文改写了流程含义。

21. 文件：`11_appendix_timing_structures.yaml`
    位置：输出行 25、32、43、58、62、73、91、100、109、120、124
    原文：`Paid ability window: ...`
    译文：`支付型能力窗口：...`
    原因：术语表固定译法为“付费能力窗口”，该文件系统性使用了不一致的术语。

## 结论

- 当前产物已经具备“全量输出文件存在、基础 YAML 可读取”的状态，但离“可验收的高质量译稿”仍有明显距离。
- 最需要优先返工的是 `09_abilities.yaml`，因为它同时存在结构损坏、字段丢失和漏译三类高优先级问题。
- 第二优先级是 `07_access_breach.yaml`、`08_card_manipulation.yaml`、`10_additional_rules.yaml`、`11_appendix_timing_structures.yaml`，这些文件的问题主要集中在卡名映射、特殊标记保留、固定术语和局部语义偏差。
- `02_parts_of_a_card.yaml`、`03_card_types.yaml`、`05_turns.yaml`、`06_runs.yaml` 本轮未确认出明确问题，但建议在后续返工时一并做一次统一术语回扫。
