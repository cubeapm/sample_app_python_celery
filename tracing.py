import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter


def init_tracing():
    provider = TracerProvider()
    if os.getenv('OTEL_LOG_LEVEL', '') == 'debug':
        processor = SimpleSpanProcessor(ConsoleSpanExporter())
    else:
        processor = BatchSpanProcessor(OTLPSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
