# TRANSLATION_REPORT

## 总结

- 已完成文件数：11 / 11
- 已完成条目数：1910 / 1910
- 评审状态：已完成全文翻译、结构标签检查、术语一致性检查、卡牌标签可解析性检查，以及残留英文人工复核。
- 最终结论：在修复本轮评审发现的问题后，未发现剩余的未解决翻译错误。

## 评审方法

- 逐文件确认 `translation/yaml2json/` 中所有 `translation` 字段均已填写。
- 使用 `scripts/translation_audit.py` 检查未翻译项、结构标签、括号/标记一致性。
- 使用参考资料核对所有 `{card:...}` 标签是否可解析。
- 人工扫描术语一致性、残留英文、章节标题与时序表结构。

## 已发现并修复的问题

1. 位置：`translation/yaml2json/02_parts_of_a_card.json` / `rule_identity_subtypes` 等 5 处子类别列表
   原文：列表中包含 `{n}...{/n}` 结构标签。
   修正前译文：遗漏了 `{n}...{/n}`。
   原因：结构标签未保留，会造成渲染结构与原文不一致。
   修正后：已在 `rule_identity_subtypes`、`rule_agenda_subtypes`、`rule_asset_subtypes`、`rule_ice_subtypes`、`rule_operation_subtypes` 中补回对应标签。

2. 位置：`translation/yaml2json/03_card_types.json` 等多处
   原文：`play area`
   修正前译文：`游玩区`
   原因：与项目后续章节统一采用的“游戏区”不一致。
   修正后：统一改为 `游戏区`。

3. 位置：`translation/yaml2json/01_game_concepts.json` 等多处
   原文：`nested cost`
   修正前译文：`内嵌费用`
   原因：与项目后续章节统一采用的“内部费用”不一致。
   修正后：统一改为 `内部费用`。

4. 位置：`translation/yaml2json/09_abilities.json` / `rule_play_ability`
   原文：`event or operation`
   修正前译文：`事件牌或行动牌`
   原因：与第 3 章中公司牌类别“事务”的译法不一致。
   修正后：统一改为 `事件牌或事务`，并同步修正相关条目中的“行动牌”。

5. 位置：`translation/yaml2json/06_runs.json` / `rule_initiation_bad_publicity`
   原文：`credits are added to the Runner's bad publicity fund`
   修正前译文：`每有公司 1 枚负面宣传标记，就向潜袭者的负面宣传资金池中加入 1[c]。`
   原因：译文擅自补入了原文未写出的具体数值与图标。
   修正后译文：`会向潜袭者的负面宣传资金池加入信用点。`

6. 位置：`translation/yaml2json/07_access_breach.json` / `rule_prohibiting_access-1-example`
   原文：`other than Ash`
   修正前译文：`除 Ash 之外`
   原因：正文残留英文卡名。
   修正后译文：`除{card:Ash 2X3ZB9CY}之外`

7. 位置：`translation/yaml2json/09_abilities.json` / `rule_condition_requirements_part_of_effect-1-example`
   原文：`installing the Dyson Mem Chip ... give them 1 credit`
   修正前译文：`安装这张 Dyson Mem Chip ... 给予其 1[c]`
   原因：正文残留英文卡名，且把文字形式的 `1 credit` 误写成了图标形式 `1[c]`。
   修正后译文：`安装这张{card:Dyson Mem Chip} ... 给予其1点信用点`

8. 位置：`translation/yaml2json/09_abilities.json` / `rule_expected_effects`、`rule_lingering_effect`、`rule_dependent_effects`、`rule_mode_definition`
   原文：`{term:expected effects}`、`{term:lingering effects}`、`{term:depends on}`、`{term:modal abilities}`
   修正前译文：上述 `term` 标签内容仍为英文。
   原因：术语标签未完全本地化。
   修正后：分别改为 `{term:预期效果}`、`{term:残留效果}`、`{term:依赖于}`、`{term:模式能力}`。

9. 位置：`translation/yaml2json/10_additional_rules.json` / `rule_suffer_or_take_damage`、`rule_bad_publicity_fund`
   原文：`{term:suffers}`、`{term:takes}`、`{term:bad publicity fund}`
   修正前译文：对应 `term` 标签内容仍为英文。
   原因：术语标签未完全本地化。
   修正后：分别改为 `{term:承受}`、`{term:受到}`、`{term:负面宣传资金池}`。

10. 位置：`translation/yaml2json/10_additional_rules.json` / `rule_bluffing-1-example`
    原文：`their first click`、`For their second click`
    修正前译文：`第一个[click]`、`第二个[click]`
    原因：把正文里的英文单词 `click` 错写成了图标标记。
    修正后译文：`第一个点击`、`第二个点击`

11. 位置：`translation/yaml2json/10_additional_rules.json` / `rule_dividends`，以及同文件若干示例
    原文：`"Dividends N" means ...`
    修正前译文：关键词解释句仍大段保留英文；另有 `Femme`、`Jesminder`、`Argus Security` 等英文昵称残留。
    原因：漏译正文说明文字。
    修正后：将定义句完整译为中文，并把相关英文昵称改回中文名或完整卡牌标签。

12. 位置：`translation/yaml2json/11_appendix_timing_structures.json`
    原文：章节标题包含 `{ref:...}`，且 `before "end the run"` 含有显式短语引用。
    修正前译文：多个标题遗漏 `{ref:...}`；一处保留 `end the run` 英文短语。
    原因：结构标签遗漏，且存在正文残留英文。
    修正后：补回各标题的 `{ref:...}`，并改为 `“终止本次潜袭”`。

## 自动审计剩余提示

- `scripts/translation_audit.py` 仍报告少量 `ascii_in_tags`。
- 经人工复核，这些均为可接受的误报，主要来自以下情况：
  - 官方中文卡名本身含有拉丁字符或数字，例如 `DJ芬里斯`、`DNA追迹者`、`LLDS能量调节器`、`T400记忆钻石`、`尘埃2X3ZB9CY`、`次代II型`、`约书亚B.`、`realloc()`。
  - 特殊结构标签本身必须保留英文机器可读内容，例如 `{ref/through:...}` 与 `{link:...}`。
- 审计中剩余的 2 条 `bracket_token_mismatch` 位于第 1 章：
  - `rule_lose_credits-1-example`
  - `rule_memory_check_mu_restrictions`
  这两处已人工核对，译文未新增或遗漏任何实际规则标记，属于脚本对空格与标点写法的误报。

## 最终结论

- 所有 1910 个可翻译条目均已完成。
- 本轮评审发现的问题均已修复。
- 当前版本可以进入后续生成网页或进一步排版校对阶段。
